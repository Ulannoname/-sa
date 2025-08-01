function changeById() {
    let title = document.getElementById("title");
    title.textContent = "С помощью getld";
    title.style.color = "red";
}

function changeByClass() {
  let text = document.getElementsByClassName("text");
  text[0].textContent = "Первый класс изменен!";
  text[1].style.color = "green";
}