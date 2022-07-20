const plus = (id) => {
  const element = document.getElementById(id);
  let interest = element.innerText;
  interest++;
  document.getElementById(id).innerText = interest;
  const { data } = axios.post("/", { id, interest });
  console.log(data);
};

const minus = (id) => {
  const element = document.getElementById(id);
  let interest = element.innerText;
  interest--;
  document.getElementById(id).innerText = interest;
  const { data } = axios.post("/", { id, interest });
};
