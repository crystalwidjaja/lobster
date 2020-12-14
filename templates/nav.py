<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href='/static/home.css' />
    <link href='/all.html' />
    <title>{{title}}</title>
</head>
<!-- Navigation bar with dropdown menu and items -->
<!-- <nav> element represents this section of the page -->
<nav class="navbar navbar-expand-lg navbar-light " style="background-color: #add8e6; font-family:times new roman;">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand" href="/">Home</a>
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
            <li class="nav-item">
                <div class="dropdown" style="align: float; font-family:times new roman;">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Portfolio
                    </button>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton"> <!-- <a> tag designates hyperlink -->
                        <a class="dropdown-item" href="http://127.0.0.1:3000/sub">Project Plan</a>
                        <a class="dropdown-item" href="/trivia">Trivia Game</a>
                        <a class="dropdown-item" href="/guess_the_number">Guess The Number</a>
                        <a class="dropdown-item" href="/hangman">Hangman</a>
                        <a class="dropdown-item" href="/reaction_time">Reaction Time</a>
                        <a class="dropdown-item" href="/rps">RPS</a>
                        <a class="dropdown-item" href="/madlibs">Mad Libs</a>
                        <a class="dropdown-item" href="/all">All Games</a>
                    </div>
                </div>
            </li>
            <li class="nav-item active">
                <a href="/about" class="btn btn-outline-secondary btn-sm" style="margin-left: 10px; margin-right: 10px; margin-top: 5px; font-family:times new roman;">About Us</a>
            </li>
            <li>
                <p style="color: black; text-align: left; margin-left: 820px; margin-top: 6px; margin-bottom: 0px;">Lobsters</p>
            </li>
        </ul>
    </div>
</nav>
