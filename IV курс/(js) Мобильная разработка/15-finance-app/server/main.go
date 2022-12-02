package main

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	e.Use(middleware.CORS())

	e.POST("/login", login)

	r := e.Group("/api")
	r.Use(middleware.JWTWithConfig(middleware.JWTConfig{
		SigningKey: []byte("secret"),
	}))

	r.GET("/costs", getAllCosts)
	r.POST("/costs", createCosts)
	r.DELETE("/costs/:id", deleteCosts)
	r.GET("/earnings", getAllEarnings)
	r.POST("/earnings", createEarnings)
	r.DELETE("/earnings/:id", deleteEarnings)

	e.Logger.Fatal(e.Start(":1323"))
}
