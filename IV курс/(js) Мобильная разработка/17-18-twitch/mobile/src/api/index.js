import axios from "axios";

class Api {
    constructor() {
        this.baseURL = "http://192.168.137.1:1323"
        this.client = axios.create({baseURL: this.baseURL})
    }

    async logIn(username, password) {
        return await this.client.post("/auth/log-in", {username: username, password: password})
    }

    async getUserinfo(access_token) {
        return await this.client.get("/api/userinfo", {headers: this.makeHeaders(access_token)})
    }

    async getFollows(access_token) {
        return await this.client.get("/api/follows", {headers: this.makeHeaders(access_token)})
    }

    async getRecords(access_token) {
        return await this.client.get("/api/records", {headers: this.makeHeaders(access_token)})
    }

    async getRecommendations(access_token) {
        return await this.client.get("/api/recommendations", {headers: this.makeHeaders(access_token)})
    }

    makeHeaders(access_token) {
        return {"Authorization": `Bearer ${access_token}`}
    }
}

const api = new Api();
export default api;
