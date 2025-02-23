package main

import (
	"fmt"
	"log"

	"github.com/gin-gonic/gin"
)

func main() {

	r := gin.Default()

	err := r.Run("0.0.0.0:3000")
	if err != nil {
		log.Fatal("Error starting server: ", err)
	}
	fmt.Println("Server is up!")
}
