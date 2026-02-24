class ResponseService extends Service {
    constructor() {
        super();
        this.initConfig('../core/app.config.json');
    }

    async get() {
        return super.fetchAResource("/api/response", "GET");
    }
    
    async getByID(id) {
        return super.fetchAResource(`/api/response/${id}`, "GET");
    }
    
    async save(id, payload) {
        return super.fetchAResource(`/api/response/${id}`, "POST", {}, payload);
    }

    async update(id, payload) {
        return super.fetchAResource(`/api/response/${id}`, "PATCH", {}, payload);
    }

    async select(id) {
        return super.fetchAResource(`/api/response/select/${id}`, "PATCH", {}, {});
    }
    
    async delete(id) {
        return super.fetchAResource(`/api/response/${id}`, "DELETE");
    }

    async saveRessource(body) {
        return super.fetchAResource('api/upload', 'POST', {}, body);
    }

}
