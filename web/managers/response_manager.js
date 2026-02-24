async function getApis(){
    
    try{
        let response = await appApiService.get();

        if(response != null){
			return response;
        }

    } catch(error){
        console.log(error)
        alert("An error occured!");
    }
}

async function createResponse(api_id, json) {
    
    try{
        let response = await appResponseService.save(api_id, {
            json: json,
        });

        if(response != null){
            return response;
        }

    } catch(Error){
        console.log(Error);
        alert("An error occured!");
    }
}

async function updateResponse(id, json) {
    
    try{
        let response = await appResponseService.update(id, {
            json: json,
        });

        if(response != null){
            return response;
        }

    } catch(Error){
        console.log(Error);
        alert("An error occured!");
    }
}

async function removeResponse(id){
    
    try{
        await appResponseService.delete(id);

    } catch(Error){
        alert("An error occured!");
    }
}

async function switchResponse(id){
    
    try{
        await appResponseService.select(id);

    } catch(Error){
        alert("An error occured!");
    }
}

async function uploadRessource(file) {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:1901/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Upload failed: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error(error);
        alert("An error occurred during upload!");
        return null;
    }
}
