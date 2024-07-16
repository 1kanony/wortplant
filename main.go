package main

import (
	"encoding/csv"
	"fmt"
	"github.com/sajari/fuzzy"
	"log"
	"os"
	"strings"
)

func main() {
	model := fuzzy.NewModel()

	file, err := os.Open("sample.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Create a new CSV reader
	reader := csv.NewReader(file)

	// Read all records
	records, err := reader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	// For testing only, this is not advisable on production
	model.SetThreshold(1)

	// This expands the distance searched, but costs more resources (memory and time).
	// For spell checking, "2" is typically enough, for query suggestions this can be higher
	model.SetDepth(5)

	if len(records) == 0 {
		return
	}

	words := records[0]

	// Train multiple words simultaneously by passing an array of strings to the "Train" function
	model.Train(words)

	var wort string

	for {
		_, err := fmt.Scan(&wort)
		if err != nil {
			return
		}

		if strings.ToLower(wort) == "quit" {
			break
		}

		fmt.Println(model.SpellCheck(wort))
	}
}
