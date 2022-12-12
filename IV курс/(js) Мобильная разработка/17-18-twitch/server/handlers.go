package main

import (
	"github.com/golang-jwt/jwt"
	"github.com/labstack/echo/v4"
	"net/http"
	"sync"
	"time"
)

type (
	Credentials struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}
	Userinfo struct {
		ID       int    `json:"id"`
		Username string `json:"username"`
		Avatar   string `json:"avatar"`
	}
	channel struct {
		ID     int    `json:"id"`
		Name   string `json:"name"`
		Avatar string `json:"avatar"`
	}
	stream struct {
		ID       int      `json:"id"`
		Title    string   `json:"title"`
		Category string   `json:"category"`
		Tags     []string `json:"tags"`
		Preview  string   `json:"preview"`
		Viewers  int      `json:"viewers"`
	}
	Follow struct {
		ID      int      `json:"id"`
		Active  bool     `json:"active"`
		Channel *channel `json:"channel"`
		Stream  *stream  `json:"stream"`
		Updates int      `json:"updates"`
	}
	Record struct {
		ID       int      `json:"id"`
		Channel  *channel `json:"channel"`
		Title    string   `json:"title"`
		Category string   `json:"category"`
		Preview  string   `json:"preview"`
		Since    int      `json:"since"`
	}
	Recommendation struct {
		ID      int      `json:"id"`
		Channel *channel `json:"channel"`
		Stream  *stream  `json:"stream"`
	}
)

var (
	lock     = sync.Mutex{}
	userinfo = &Userinfo{
		ID:       0,
		Username: "belo4ya",
		Avatar:   "/avatar.jpg",
	}
	follows = []*Follow{
		{
			ID:     0,
			Active: true,
			Channel: &channel{
				ID:     0,
				Name:   "melharucos",
				Avatar: "/melharucos.png",
			},
			Stream: &stream{
				ID:       0,
				Title:    "Последняя неделя года !atom !планы !boosty",
				Category: "Общение",
				Tags:     []string{"Русский"},
				Preview:  "/preview.jpg",
				Viewers:  111,
			},
			Updates: 0,
		},
		{
			ID:     1,
			Active: true,
			Channel: &channel{
				ID:     1,
				Name:   "just_ns",
				Avatar: "/avatar.jpg",
			},
			Stream: &stream{
				ID:       1,
				Title:    "VP vs GG !tg !yt",
				Category: "Dota 2",
				Tags:     []string{"Русский"},
				Preview:  "/preview.jpg",
				Viewers:  6255,
			},
			Updates: 0,
		},
		{
			ID:     2,
			Active: true,
			Channel: &channel{
				ID:     2,
				Name:   "DreadzTV",
				Avatar: "/avatar.jpg",
			},
			Stream: &stream{
				ID:       2,
				Title:    "Олег вернет все | t.me/realknp",
				Category: "Mount & Blade II: Bannerlord",
				Tags:     []string{"Русский"},
				Preview:  "/preview.jpg",
				Viewers:  1329,
			},
			Updates: 0,
		},
		{
			ID:     3,
			Active: false,
			Channel: &channel{
				ID:     3,
				Name:   "DreadzTV",
				Avatar: "/dreadz-tv.png",
			},
			Stream:  nil,
			Updates: 5,
		},
		{
			ID:     4,
			Active: false,
			Channel: &channel{
				ID:     4,
				Name:   "DreadzTV",
				Avatar: "/dreadz-tv.png",
			},
			Stream:  nil,
			Updates: 3,
		},
		{
			ID:     5,
			Active: false,
			Channel: &channel{
				ID:     5,
				Name:   "DreadzTV",
				Avatar: "/dreadz-tv.png",
			},
			Stream:  nil,
			Updates: 0,
		},
	}
	records = []*Record{
		{
			ID: 0,
			Channel: &channel{
				ID:     0,
				Name:   "just_ns",
				Avatar: "/avatar.jpg",
			},
			Title:    "VP vs GG !tg !yt",
			Category: "Dota 2",
			Preview:  "/preview.jpg",
			Since:    1,
		},
		{
			ID: 1,
			Channel: &channel{
				ID:     1,
				Name:   "just_ns",
				Avatar: "/avatar.jpg",
			},
			Title:    "VP vs GG !tg !yt",
			Category: "Dota 2",
			Preview:  "/preview.jpg",
			Since:    2,
		},
	}
	recommendations = []*Recommendation{
		{
			ID: 0,
			Channel: &channel{
				ID:     0,
				Name:   "watsondoto",
				Avatar: "/avatar.jpg",
			},
			Stream: &stream{
				ID:       0,
				Title:    "я болею 1 rank 12kmmr !tg !inst",
				Category: "Dota 2",
				Tags:     []string{"Русский"},
				Preview:  "/preview.jpg",
				Viewers:  3662,
			},
		},
		{
			ID: 1,
			Channel: &channel{
				ID:     1,
				Name:   "watsondoto",
				Avatar: "/avatar.jpg",
			},
			Stream: &stream{
				ID:       1,
				Title:    "я болею 1 rank 12kmmr !tg !inst",
				Category: "Dota 2",
				Tags:     []string{"Русский"},
				Preview:  "/preview.jpg",
				Viewers:  3662,
			},
		},
	}
)

func logIn(c echo.Context) error {
	creds := &Credentials{}
	if err := c.Bind(creds); err != nil {
		return err
	}
	if creds.Username != "belo4ya" || creds.Password != "belo4ya" {
		return echo.ErrUnauthorized
	}

	token := jwt.NewWithClaims(
		jwt.SigningMethodHS256,
		jwt.StandardClaims{
			ExpiresAt: time.Now().Add(5 * time.Hour).Unix(),
		},
	)
	t, err := token.SignedString([]byte("secret"))
	if err != nil {
		return err
	}

	return c.JSON(http.StatusOK, echo.Map{
		"access_token": t,
	})
}

func getUserinfo(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	return c.JSON(http.StatusOK, userinfo)
}

func getFollows(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	return c.JSON(http.StatusOK, follows)
}

func getRecords(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	return c.JSON(http.StatusOK, records)
}

func getRecommendations(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	return c.JSON(http.StatusOK, recommendations)
}
