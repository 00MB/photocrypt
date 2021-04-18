const thisForm = document.getElementById("form");
thisForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(thisForm).entries();
  document.getElementById("demo").innerHTML = "Hello World!";
  console.log(formData);
  const response = await fetch(
    "https://photocrypthack.herokuapp.com/https://www.vippng.com/png/detail/320-3209103_200-kb-download-tree-with-transparent-background-clipart.png/true/true/10",
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    }
  );

  const result = await response.json();
  console.log(result);
});
// var button = document.getElementById("submit");
// if (!button) {
//   console.log("works");
// }
// button.addEventListener("click", function (e) {
//   e.preventDefault();
//   console.log("hey");
//   const req = new XMLHttpRequest();
//   const baseUrl =
//     "https://photocrypthack.herokuapp.com/https://www.vippng.com/png/detail/320-3209103_200-kb-download-tree-with-transparent-background-clipart.png/true/true/10";
// });
