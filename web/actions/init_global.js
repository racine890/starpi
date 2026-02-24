// We create an instance of each service if there is not
if(typeof DataManager != 'undefined'){
    appDataManager = new DataManager();
    appPersistentDataManager = new DataManager(true);
}
if(typeof ApiService != 'undefined')
    appApiService = new ApiService();
if(typeof ResponseService != 'undefined')
    appResponseService = new ResponseService();
