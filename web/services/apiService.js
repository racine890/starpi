class ApiService extends Service {
    constructor(){
        super();
        this.initConfig('../core/app.config.json');
    }

    async get(){
        return super.fetchAResource("/api/api", "GET");
    }
    
    async save(payload){
        return super.fetchAResource(`/api/api`, "POST", {}, payload);
    }

    async update(id, payload){
        return super.fetchAResource(`/api/api/${id}`, "PATCH", {}, payload);
    }
    
    async delete(id){
        return super.fetchAResource(`/api/api/${id}`, "DELETE");
    }

    async start_or_stop(id){
        return super.fetchAResource(`/api/api/switch/${id}`, "PATCH", {}, {});
    }
}
