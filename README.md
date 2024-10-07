# habitica.js
Mobile-API for [habitica](https://play.google.com/store/apps/details?id=com.habitrpg.android.habitica) mobile game

## Example
```JavaScript
async function main() {
	const { Habitica } = require("./habitica.js")
	const habitica = new Habitica()
	await habitica.login("userName", "password")
}

main()
```
