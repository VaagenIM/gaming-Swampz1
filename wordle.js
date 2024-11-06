const words = ["apple", "grape", "peach", "berry", "mango", "lemon", "plumb"];
let solution = words[Math.floor(Math.random() * words.length)];
let attempts = 6;

function makeGuess() {
  const guessInput = document.getElementById("guessInput");
  const feedback = document.getElementById("feedback");
  let guess = guessInput.value.toLowerCase();

  if (guess.length !== 5) {
    alert("Please enter a 5-letter word.");
    return;
  }

  if (attempts <= 0) {
    feedback.innerHTML = `<p>Game Over! The word was <strong>${solution}</strong>.</p>`;
    return;
  }

  attempts--;

  const result = checkGuess(guess);
  displayResult(result);

  if (guess === solution) {
    feedback.innerHTML = `<p class="result correct">Congratulations! You guessed the word: <strong>${solution}</strong></p>`;
  } else if (attempts === 0) {
    feedback.innerHTML = `<p class="result">No more attempts! The word was <strong>${solution}</strong>.</p>`;
  } else {
    feedback.innerHTML += `<p>${attempts} attempt(s) left.</p>`;
  }

  guessInput.value = "";
}

function checkGuess(guess) {
  let result = [];
  for (let i = 0; i < 5; i++) {
    if (guess[i] === solution[i]) {
      result.push({ letter: guess[i], status: "correct" });
    } else if (solution.includes(guess[i])) {
      result.push({ letter: guess[i], status: "present" });
    } else {
      result.push({ letter: guess[i], status: "absent" });
    }
  }
  return result;
}

function displayResult(result) {
  const feedback = document.getElementById("feedback");
  let resultHtml = "<div class='guess'>";
  result.forEach(item => {
    resultHtml += `<span class="${item.status}">${item.letter.toUpperCase()}</span> `;
  });
  resultHtml += "</div>";
  feedback.innerHTML += resultHtml;
}
