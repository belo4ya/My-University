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
	e.Use(middleware.Static("static"))

	auth := e.Group("/auth")
	auth.POST("/log-in", logIn)

	api := e.Group("/api")
	api.Use(middleware.JWTWithConfig(middleware.JWTConfig{
		SigningKey: []byte("secret"),
	}))

	api.GET("/userinfo", getUserinfo)
	api.GET("/follows", getFollows)
	api.GET("/records", getRecords)
	api.GET("/recommendations", getRecommendations)

	e.Logger.Fatal(e.Start(":1323"))
}
