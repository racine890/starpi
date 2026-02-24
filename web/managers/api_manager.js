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

async function createApi(name, url, method, responseType) {
    
    try{
        let response = await appApiService.save({
            name: name,
            url: url,
            method: method,
            responseType: responseType,
        });

        if(response != null){
            return response;
        }

    } catch(Error){
        console.log(Error);
        alert("An error occured!");
    }
}

async function updateApi(id, name, url, method, responseType) {
    
    try{
        let response = await appApiService.update(id, {
            name: name,
            url: url,
            method: method,
            responseType: responseType,
        });

        if(response != null){
            return response;
        }

    } catch(Error){
        console.log(Error);
        alert("An error occured!");
    }
}

async function removeApi(id){
    
    try{
        await appApiService.delete(id);

    } catch(Error){
        alert("An error occured!");
    }
}

async function startStopApi(response_id){
    
    try{

        if (appDataManager.checkvar('started')){
            let started = new Set(appDataManager.getvar('started'));
            if (started.has(response_id)) {
                started.delete(response_id);
            } else {
                started.add(response_id);
            }
            appDataManager.setvar('started', [...started]);
        }

        await appApiService.start_or_stop(response_id);

    } catch(Error){
        alert("An error occured!");
    }
}