const like = (id) => {
  star = id;
  const { data } = axios.post("/", { star });
};
