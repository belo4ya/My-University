package main

import (
	"github.com/golang-jwt/jwt"
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"
	"sync"
	"time"
)

type (
	credentials struct {
		Username string `json:"username"`
		Password string `json:"password"`
	}

	costs struct {
		ID       int     `json:"id"`
		Amount   float64 `json:"amount"`
		Source   string  `json:"source"`
		Category string  `json:"category"`
		Datetime string  `json:"datetime"`
	}

	earnings struct {
		ID       int     `json:"id"`
		Amount   float64 `json:"amount"`
		Source   string  `json:"source"`
		Category string  `json:"category"`
		Datetime string  `json:"datetime"`
	}
)

var (
	lock = sync.Mutex{}

	costsStore = map[int]*costs{
		1: {
			ID:       1,
			Amount:   300,
			Source:   "Тинькофф",
			Category: "Еда",
			Datetime: time.Date(2022, 12, 6, 18, 25, 0, 0, time.UTC).Format(time.RFC3339),
		},
		2: {
			ID:       2,
			Amount:   200,
			Source:   "Тинькофф",
			Category: "Еда",
			Datetime: time.Date(2022, 12, 7, 7, 45, 0, 0, time.UTC).Format(time.RFC3339),
		},
		3: {
			ID:       3,
			Amount:   400,
			Source:   "Сбербанк",
			Category: "Транспорт",
			Datetime: time.Date(2022, 12, 7, 20, 30, 0, 0, time.UTC).Format(time.RFC3339),
		},
	}
	costsSeq = 4

	earningsStore = map[int]*earnings{
		1: {
			ID:       1,
			Amount:   20000,
			Source:   "Сбербанк",
			Category: "Зарплата",
			Datetime: time.Date(2022, 12, 6, 18, 25, 0, 0, time.UTC).Format(time.RFC3339),
		},
		2: {
			ID:       2,
			Amount:   22000,
			Source:   "Сбербанк",
			Category: "Зарплата",
			Datetime: time.Date(2022, 12, 7, 7, 45, 0, 0, time.UTC).Format(time.RFC3339),
		},
		3: {
			ID:       3,
			Amount:   1500,
			Source:   "Тинькофф",
			Category: "Перевод",
			Datetime: time.Date(2022, 12, 7, 20, 30, 0, 0, time.UTC).Format(time.RFC3339),
		},
	}
	earningsSeq = 4
)

func login(c echo.Context) error {
	creds := &credentials{}
	if err := c.Bind(creds); err != nil {
		return err
	}
	if creds.Username != "user" || creds.Password != "user" {
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

func getAllCosts(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	items := make([]*costs, 0, len(costsStore))
	for _, v := range costsStore {
		items = append(items, v)
	}
	return c.JSON(http.StatusOK, items)
}

func createCosts(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	item := &costs{
		ID: costsSeq,
	}
	if err := c.Bind(item); err != nil {
		return err
	}
	costsStore[item.ID] = item
	costsSeq++
	return c.JSON(http.StatusCreated, item)
}

func deleteCosts(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	id, _ := strconv.Atoi(c.Param("id"))
	delete(costsStore, id)
	return c.NoContent(http.StatusNoContent)
}

func getAllEarnings(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	items := make([]*earnings, 0, len(earningsStore))
	for _, v := range earningsStore {
		items = append(items, v)
	}
	return c.JSON(http.StatusOK, items)
}

func createEarnings(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	item := &earnings{
		ID: earningsSeq,
	}
	if err := c.Bind(item); err != nil {
		return err
	}
	earningsStore[item.ID] = item
	earningsSeq++
	return c.JSON(http.StatusCreated, item)
}

func deleteEarnings(c echo.Context) error {
	lock.Lock()
	defer lock.Unlock()
	id, _ := strconv.Atoi(c.Param("id"))
	delete(earningsStore, id)
	return c.NoContent(http.StatusNoContent)
}
