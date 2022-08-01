package main

import (
	"context"
	"fmt"
	"log"

	"google.golang.org/grpc"
	"google.golang.org/grpc/encoding/gzip"
)

type userInfoKey struct{}

type UserInfo struct {
	ID         uint32
	Name       string // Username
	CommonName string
	Givenname  string
	Surname    string
	EMail      string
}

const messageSize = 1024 * 1024 * 200 // 100MB

func main() {
	err := do()
	if err != nil {
		log.Fatal(err)
	}
}

func do() error {
	ctx := context.WithValue(context.Background(), userInfoKey{}, UserInfo{
		ID:         31415,
		Name:       "max.mustermann@example.com",
		CommonName: "Max Mustermann",
		Givenname:  "Max",
		Surname:    "Mustermann",
		EMail:      "max.mustermann@example.com",
	})

	// connect to server
	conn, err := grpc.DialContext(ctx, ":8080", grpc.WithInsecure(), grpc.WithDefaultCallOptions(grpc.MaxCallRecvMsgSize(messageSize), grpc.UseCompressor(gzip.Name)))
	if err != nil {
		return fmt.Errorf("connect to grpc server: %v", err)
	}
	c := NewRootClient(conn)

	res, err := c.Greeting(ctx, &GreetingRequest{
		Name: "Testuser",
	})
	if err != nil {
		return fmt.Errorf("greeting request: %w", err)
	}

	log.Printf("Response: %s", res.GreetedAt)

	return nil
}
