class Habitica {
	constructor(language = "en") {
		this.api = "https://habitica.com/api"
		this.language = language
		this.headers = {
			"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
			"x-client": "habitica-android",
			"x-user-timezoneoffset": "-480"
		}
	}

	async login(userName, password) {
		const response = await fetch(
			`${this.api}/v4/user/auth/local/login`, {
				method: "POST",
				body: JSON.stringify({
					password: password,
					username: userName
				}),
				headers: this.headers
			})
		const data = await response.json()
		this.userId = data.data.id
		this.apiToken = data.data.api_token
		this.headers["x-api-user"] = this.userId
		this.headers["x-api-key"] = this.apiToken
		return data
	}

	async register(email, password, username) {
		const response = await fetch(
			`${this.api}/v4/user/auth/local/register`, {
				method: "POST",
				body: JSON.stringify({
					confirmPassword: password,
					email: email,
					password: password,
					username: userName
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getCurrentUser() {
		const response = await fetch(
			`${this.api}/v4/user`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getAppRewards() {
		const response = await fetch(
			`${this.api}/v4/user/in-app-rewards`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getWorldState() {
		const response = await fetch(
			`${this.api}/v4/world-state`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGroupPlans() {
		const response = await fetch(
			`${this.api}/v4/group-plans`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTasks() {
		const response = await fetch(
			`${this.api}/v4/tasks/user`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getConversations() {
		const response = await fetch(
			`${this.api}/v4/inbox/conversations`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async updateUsername(userName) {
		const response = await fetch(
			`${this.api}/v4/user/auth/update-username`, {
				method: "PUT",
				body: JSON.stringify({
					username: userName
				}),
				headers: this.headers
			})
		return response.json()
	}

	async updateEmail(email, password) {
		const response = await fetch(
			`${this.api}/v4/user/auth/update-email`, {
				method: "PUT",
				body: JSON.stringify({
					password: password,
					newEmail: email
				}),
				headers: this.headers
			})
		return response.json()
	}

	async updatePassword(oldPassword, newPassword) {
		const response = await fetch(
			`${this.api}/v4/user/auth/update-password`, {
				method: "PUT",
				body: JSON.stringify({
					confirmPassword: newPassword,
					newPassword: newPassword,
					password: oldPassword
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getMarketGears() {
		const response = await fetch(
			`${this.api}/v4/shops/market-gear?lang=${this.language}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getMarket() {
		const response = await fetch(
			`${this.api}/v4/shops/market?lang=${this.language}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async buyItem(itemName) {
		const response = await fetch(
			`${this.api}/user/buy/${itemName}`, {
				method: "POST",
				body: JSON.stringify({
					quantity: 1
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getQuests() {
		const response = await fetch(
			`${this.api}/v4/shops/quests?lang=${this.language}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTimeTravelers() {
		const response = await fetch(
			`${this.api}/v4/shops/time-travelers?lang=${this.language}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async equipItem(itemName) {
		const response = await fetch(
			`${this.api}/v4/user/equip/equipped/${itemName}`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getGroupInfo(groupId) {
		const response = await fetch(
			`${this.api}/v4/groups/${groupId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGroupChat(groupId) {
		const response = await fetch(
			`${this.api}/v4/groups/${groupId}/chat`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async sendMessage(groupId, message) {
		const response = await fetch(
			`${this.api}/v4/groups/${groupId}/chat`, {
				method: "POST",
				body: JSON.stringify({
					message: message
				}),
				headers: this.headers
			})
		return response.json()
	}

	async deleteMessage(groupId, messageId) {
		const response = await fetch(
			`${this.api}/v4/groups/${groupId}/chat/${messageId}`, {
				method: "DELETE",
				headers: this.headers
			})
		return response.json()
	}

	async leaveFromGroup(groupId) {
		const response = await fetch(
			`${this.api}/v4/groups/${groupId}/leave?keepChallenges=leave-challenges`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getUserProfile(userId) {
		const response = await fetch(
			`${this.api}/v4/members/${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async sendPrivateMessage(userId, message) {
		const response = await fetch(
			`${this.api}/v4/members/send-private-message`, {
				method: "POST",
				body: JSON.stringify({
					message: message,
					toUserId: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getConversationMessages(conversationId, page = 0) {
		const response = await fetch(
			`${this.api}/v4/inbox/messages?conversation=${conversationId}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async blockUser(userId) {
		const response = await fetch(
			`${this.api}/v4/user/block/${userId}`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async getChallenges(page = 0) {
		const response = await fetch(
			`${this.api}/v4/challenges/user?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getChallengeInfo(challengeId) {
		const response = await fetch(
			`${this.api}/v4/challenges/${challengeId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async joinChallenge(challengeId) {
		const response = await fetch(
			`${this.api}/v4/challenges/${challengeId}/join`, {
				method: "POST",
				headers: this.headers
			})
		return response.json()
	}

	async leaveChallenge(challengeId, keep = "remove-all") {
		const response = await fetch(
			`${this.api}/v4/challenges/${challengeId}/leave`, {
				method: "POST",
				body: JSON.stringify({
					keep: keep
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getUserAchievements(userId) {
		const response = await fetch(
			`${this.api}/v4/members/${userId}/achievements?lang=${this.language}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getStatus() {
		const response = await fetch(
			`${this.api}/v4/status`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {Habitica}
