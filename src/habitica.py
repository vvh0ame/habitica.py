import requests

class Habitica:
	def __init__(self, language: str = "en"):
		self.api = "https://habitica.com/api"
		self.headers = {
			"user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)",
			"x-client": "habitica-android",
			"x-user-timezoneoffset": "-480"
		}
		self.language = language

	def login(self, username: str, password: str):
		data = {
			"password": password,
			"username": username
		}
		response = requests.post(
			f"{self.api}/v4/user/auth/local/login",
			data=data,
			headers=self.headers).json()
		if "data" in response:
			self.user_id = response["data"]["id"]
			self.api_token = response["data"]["apiToken"]
			self.headers["x-api-user"] = self.user_id
			self.headers["x-api-key"] = self.api_token
		return response

	def register(
			self,
			email: str,
			password: str,
			username: str):
		data = {
			"confirmPassword": password,
			"email": email,
			"password": password,
			"username": username
		}
		return requests.post(
			f"{self.api}/v4/user/auth/local/register",
			data=data,
			headers=self.headers).json()

	def get_current_user(self):
		return requests.get(
			f"{self.api}/v4/user",
			headers=self.headers).json()

	def get_app_rewards(self):
		return requests.get(
			f"{self.api}/v4/user/in-app-rewards",
			headers=self.headers).json()

	def get_world_state(self):
		return requests.get(
			f"{self.api}/v4/world-state",
			headers=self.headers).json()

	def get_group_plans(self):
		return requests.get(
			f"{self.api}/v4/group-plans",
			headers=self.headers).json()

	def get_tasks(self):
		return requests.get(
			f"{self.api}/v4/tasks/user",
			headers=self.headers).json()

	def get_conversations(self):
		return requests.get(
			f"{self.api}/v4/inbox/conversations",
			headers=self.headers).json()

	def update_username(self, username: str):
		data = {
			"username": username
		}
		return requests.put(
			f"{self.api}/v4/user/auth/update-username",
			data=data,
			headers=self.headers).json()

	def update_email(self, email: str, password: str):
		data = {
			"password": password,
			"newEmail": email
		}
		return requests.put(
			f"{self.api}/v4/user/auth/update-email",
			data=data,
			headers=self.headers).json()

	def update_password(
			self,
			old_password: str,
			new_password: str):
		data = {
			"confirmPassword": new_password,
			"newPassword": new_password,
			"password": new_password
		}
		return requests.put(
			f"{self.api}/v4/user/auth/update-password",
			data=data,
			headers=self.headers).json()

	def edit_profile(
			self,
			profile_name: str = None,
			profile_bio: str = None,
			profile_image_url: str = None,
			use_costume: bool = False,
			auto_equip: bool = True,
			avatar_size: str = "slim",
			avatar_shirt_color: str = None,
			avatar_skin_color: str = None,
			avatar_hair_color: str = None,
			avatar_hair_base: int = None,
			avatar_hair_bangs: int = None,
			avatar_chair_color: str = None):
		data = {}
		if profile_name:
			data["profile.name"] = profile_name
		if profile_bio:
			data["profile.blurb"] = profile_bio
		if profile_image_url:
			data["profile.imageUrl"] = profile.imageUrl
		if use_costume:
			data["preferences.costume"] = use_costume
		if auto_equip:
			data["preferences.autoEquip"] = auto_equip
		if avatar_size:
			data["preferences.size"] = avatar_size
		if avatar_shirt_color:
			data["preferences.shirt"] = avatar_shirt_color
		if avatar_skin_color:
			data["preferences.skin"] = avatar_skin_color
		if avatar_hair_color:
			data["preferences.hair.color"] = avatar_hair_color
		if avatar_hair_base:
			data["preferences.hair.base"] = avatar_hair_base
		if avatar_hair_bangs:
			data["preferences.hair.bangs"] = avatar_hair_bangs
		if avatar_chair_color:
			data["preferences.chair"] = avatar_chair_color
		return requests.put(
			f"{self.api}/v4/user",
			data=data,
			headers=self.headers).json()

	def get_market_gear(self):
		return requests.get(
			f"{self.api}/v4/shops/market-gear?lang={self.language}",
			headers=self.headers).json()

	def get_market(self):
		return requests.get(
			f"{self.api}/v4/shops/market?lang={self.language}",
			headers=self.headers).json()

	def buy_item(self, item_name: str):
		data = {
			"quantity": 1
		}
		return requests.post(
			f"{self.api}/user/buy/{item_name}",
			data=data,
			headers=self.headers).json()

	def get_quests(self):
		return requests/get(
			f"{self.api}/v4/shops/quests?lang={self.language}",
			headers=self.headers).json()

	def get_time_travelers(self):
		return requests.get(
			f"{self.api}/v4/shops/time-travelers?lang={self.language}",
			headers=self.headers).json()

	def equip_item(self, item_name: str):
		return requests.post(
			f"{self.api}/v4/user/equip/equipped/{item_name}",
			headers=self.headers).json()

	def create_group(
			self,
			name: str,
			description: str,
			type: str = "party",
			only_leader_challenges: bool = False,
			only_leader_gets_gems: bool = False):
		data = {
			"name": name,
			"description": description,
			"type": type,
			"leader": self.user_id,
			"leaderOnly": {
				"challenges": only_leader_challenges,
				"getGems": only_leader_gets_gems
			}
		}
		return requests.post(
			f"{self.api}/v4/groups",
			data=data,
			headers=self.headers).json()

	def get_group_info(self, group_id: str):
		return requests.get(
			f"{self.api}/v4/groups/{group_id}",
			headers=self.headers).json()

	def get_group_chat(self, group_id: str):
		return requests.get(
			f"{self.api}/v4/groups/{group_id}/chat",
			headers=self.headers).json()
	
	def send_message(self, group_id: str, message: str):
		data = {
			"message": message
		}
		return requests.post(
			f"{self.api}/v4/groups/{group_id}/chat",
			data=data,
			headers=self.headers).json()

	def delete_message(self, group_id: str, message_id: str):
		return requests.delete(
			f"{self.api}/v4/groups/{group_id}/chat/{message_id}",
			headers=self.headers).json()

	def edit_group(
			self,
			group_id: str,
			name: str = None,
			description: str = None,
			type: str = "party",
			only_leader_challenges: bool = False,
			only_leader_gets_gems: bool = False):
		data = {}
		if name:
			data["name"] = name
		if description:
			data["description"] = description
		if type:
			data["type"] = type
		if only_leader_challenges:
			data["leaderOnly"] = {"challenges": only_leader_challenges}
		if only_leader_gets_gems:
			data["leaderOnly"] = {"getGems": only_leader_gets_gems}
		return requests.put(
			f"{self.api}/v4/groups/{group_id}",
			data=data,
			headers=self.headers).json()

	def leave_from_group(self, group_id: str):
		return requests.post(
			f"{self.api}/v4/groups/{group_id}/leave?keepChallenges=leave-challenges",
			headers=self.headers).json()

	def get_user_profile(self, user_id: str):
		return requests.get(
			f"{self.api}/v4/members/{user_id}",
			headers=self.headers).json()

	def send_private_message(self, user_id: str, message: str):
		data = {
			"message": message,
			"toUserId": user_id
		}
		return requests.post(
			f"{self.api}/v4/members/send-private-message",
			data=data,
			headers=self.headers).json()

	def get_conversation_messages(self, conversation_id: str, page: int = 0):
		return requests.get(
			f"{self.api}/v4/inbox/messages?conversation={conversation_id}&page={page}",
			headers=self.headers).json()

	def block_user(self, user_id: str):
		return requests.post(
			f"{self.api}/v4/user/block/{user_id}",
			headers=self.headers).json()

	def get_challenges(self, page: int = 0):
		return requests.get(
			f"{self.api}/v4/challenges/user?page={page}",
			headers=self.headers).json()

	def get_challenge_info(self, challenge_id: str):
		return requests.get(
			f"{self.api}/v4/challenges/{challenge_id}",
			headers=self.headers).json()

	def join_challenge(self, challenge_id: str):
		return requests.post(
			f"{self.api}/v4/challenges/{challenge_id}/join",
			headers=self.headers).json()

	def leave_challenge(self, challenge_id: str, keep: str = "remove-all"):
		data = {
			"keep": keep
		}
		return requests.post(
			f"{self.api}/v4/challenges/{challenge_id}/leave",
			data=data,
			headers=self.headers).json()

	def get_user_achievements(self, user_id: str):
		return requests.get(
			f"{self.api}/v4/members/{user_id}/achievements?lang={self.language}",
			headers=self.headers).json()

	def reset_account(self):
		return requests.post(
			f"{self.api}/v4/user/reset",
			headers=self.headers).json()

	def delete_account(self, password: str):
		data = {
			"password": password
		}
		return requests.delete(
			f"{self.api}/v4/user",
			data=data,
			headers=self.headers).json()
	
	def get_status(self):
		return requests.get(
			f"{self.api}/v4/status",
			headers=self.headers).json()
