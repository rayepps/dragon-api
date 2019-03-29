

window.dragonSettings = (function() {

  var isLocal = false

  var localApiUrl = 'http://localhost:5000'
  var sandboxApiUrl = 'https://sandbox-dragon-api.greendragon.pro'

  var localApiKey = 'localhashkey'
  var sandboxApiKey = 'f7f630753cbe4cc2be38c86c2211ef90'

  var config = {
    isLocal: isLocal,
    apiUrl: null,
    apiKey: null
  };

  config.apiUrl = config.isLocal ? localApiUrl : sandboxApiUrl
  config.apiKey = config.isLocal ? localApiKey : sandboxApiKey

  return config

})();
