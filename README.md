## A picture can tell 1000 words ... though, what about a password?  About 15 characters MAX.

## Inspiration 💡
Passwords are severely outdated. The concept of a password was created in the early 1970's before hacking and internet law were even born. **Passwords have major flaws** that are clearly visible, leading to millions of dollars lost and billions of accounts being compromised every year. The password is **often the biggest vulnerability**, due to the laziness and predictable words that can easily be fished by criminals. Passwords are also easily forgettable, **what was your first password? Can't remember? Exactly.**

## Our solution ⚙️
We have created a solution. Photocrypt is a new form of account security, currently being used through our chrome web extension, where anyone can upload a private or public image, both locally and through a URL. This image is then encrypted with **the same encryption used in Bitcoin and Ethereum**. Every passcode is unique to its image, with one single dimension being off generating an entirely different passcode. The passcode can then be customised to fit the individual sites password validation, including the addition of special characters, capital letters, and the length of the code. It is basic psychology that images are much more memorable than jumbled words. Images are a clear solution to an outdated and flawed security system, passwords can just not hold up against the ever-expanding domain of cybersecurity

## How we built it 🛠️
Our chrome extension works by receiving custom parameters about the current site validation, along with a local file upload or URL, this extension is created using JS. Once an image is submitted, the extension converts this image into a uir8 string displaying the individual pixels and colour. The flask API is then called which parses the image string. At the other end, the image is then reshaped and converted into an Ascii string [image to ascii](https://wiki.cdot.senecacollege.ca/w/imgs/thumb/R2d2.jpg/700px-R2d2.jpg.png). From there it is then encrypted using the sha256 algorithm, the most common and secure hashing algorithm in the world. This code is then passed back and formatted to fit the validation requirements, without changing the original hash encryption.
A site was also created to display this technology, which was created using flask and a MongoDB database for storing users.

## Challenges we ran into 🚧
None of us had previously worked with google chrome extensions before and only one of us had experience using Flask. This was a steep learning curve for all of us but was very beneficial. The communication was initially a struggle as well due to our poor time zones, but this is discussed later.

## Accomplishments that we're proud of 🌟
We knew coordination would be a challenge as we are an international team from 3 different continents and hence, 3 extremely different time zones. We stepped up to the challenge and made it work, by delegating each person with tasks of equal work, we managed to lower the workload all while keeping good communication all while being up to 7 hours apart. Another accomplishment we are proud of is the file upload feature, as it is a fairly complex task with chrome extensions.

## What we learned 📖
We learned all about chrome extension development, and how to create and request a REST API. We also learned about MongoDB for the first time, and how to deploy on Heroku. We finally learned the basics of encryption using the different Standard Hashing Algorithms (SHA) which is big in today's blockchain technologies.

## What's next for Photocrypt! 🚀
The next big thing for Photocrypt is its endless application and uses over many website domains, whether that is for logging into an account or for making a payment online. We wish to integrate our chrome extension further to cover areas such as video encryption. The possibilities for Photocrypt are endless!

Message Michael Beer#7583 or Angler#5664 or Roshan#9335 for any questions!
