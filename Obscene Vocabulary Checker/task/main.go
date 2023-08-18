// Obscene Vocabulary Checker (Golang)
// https://github.com/imprvhub/golang-obscenevocabularychecker-jbrains
// Project Completed By Iván Luna, August 18, 2023.
// For Hyperskill (Jet Brains Academy). Course: Introduction To Go.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode/utf8"
)

func main() {
	var fileName string
	fmt.Scan(&fileName)

	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	tabooMap := make(map[string]struct{})
	for scanner.Scan() {
		tabooWord := strings.ToLower(scanner.Text())
		if _, ok := tabooMap[tabooWord]; !ok {
			tabooMap[tabooWord] = struct{}{}
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	var word string
	fmt.Scan(&word)
	for word != "exit" {
		if _, ok := tabooMap[strings.ToLower(word)]; ok {
			word = strings.Repeat("*", utf8.RuneCountInString(word))
		}
		fmt.Println(word)

		fmt.Scan(&word)
	}

	fmt.Println("Bye!")
}
