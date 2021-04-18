const thisForm = document.getElementById("form");
thisForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(thisForm).entries();
  alert(formData);
  const response = await fetch(
    "https://photocrypthack.herokuapp.com/https://www.vippng.com/png/detail/320-3209103_200-kb-download-tree-with-transparent-background-clipart.png/true/true/10",
    {
      method: "GET",
    }
  );

  const result = await response.json();
  console.log(result);
});
