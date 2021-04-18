const thisForm = document.getElementById("form");
thisForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(thisForm);
  var url = formData.get("url");
  var chars = formData.get("chars");
  if (chars != null) {
    chars = "true";
  } else {
    chars = "false";
  }
  var caps = formData.get("caps");
  if (caps != null) {
    caps = "true";
  } else {
    chars = "false";
  }
  var length = formData.get("length");
  console.log(
    "https://photocrypthack.herokuapp.com/" +
      url +
      "/" +
      caps +
      "/" +
      chars +
      "/" +
      length
  );
  const response = await fetch(
    "https://photocrypthack.herokuapp.com/" +
      url +
      "/" +
      caps +
      "/" +
      chars +
      "/" +
      length,
    {
      mode: "no-cors",
      method: "GET",
    }
  );

  const result = await response.json();
  document.getElementById("demo").innerHTML = "Code: " + result.code;
  thisForm.reset();
});
