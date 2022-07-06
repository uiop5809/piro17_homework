const stopWatch = document.querySelector(".clock__time");
const startEl = document.querySelector(".start");
const stopEl = document.querySelector(".stop");
const resetEl = document.querySelector(".reset");

const allBtn = document.querySelector("#all");
const delBtn = document.querySelector("#del");
const recordBox = document.querySelector(".record__box");

let time = 0;

function startClock() {
  time++;
  sec = String(parseInt(time / 100)).padStart(2, "0");
  msec = String(time % 100).padStart(2, "0");
  stopWatch.textContent = `${sec}:${msec}`;
  timer = setTimeout(startClock, 10);
}

function stopClock() {
  clearTimeout(timer);
  const li = document.createElement("li");
  li.innerHTML = `
    <i class="fa-regular fa-circle"></i>
    <div>${stopWatch.textContent}</div>
  `;
  recordBox.appendChild(li);
}

function resetClock() {
  time = 0;
  clearTimeout(timer);
  stopWatch.textContent = "00:00";
}

function allCheck() {
  allBtn.classList.toggle("fa-circle-check");
  let recordList = document.querySelectorAll(".record__box li i");
  recordList.forEach((item) => {
    if (allBtn.classList.contains("fa-circle-check")) {
      item.classList.add("fa-circle-check");
    } else {
      item.classList.remove("fa-circle-check");
    }
  });
}

function delCheck() {
  recordList = document.querySelectorAll(".record__box li i");
  recordList.forEach((item) => {
    if (item.classList.contains("fa-circle-check")) {
      item.parentNode.remove();
    }
  });
}

startEl.addEventListener("click", startClock);
stopEl.addEventListener("click", stopClock);
resetEl.addEventListener("click", resetClock);

allBtn.addEventListener("click", allCheck);
delBtn.addEventListener("click", delCheck);

recordBox.addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-circle-check")) {
    e.target.classList.remove("fa-circle-check");
  } else {
    e.target.classList.add("fa-circle-check");
  }
});
