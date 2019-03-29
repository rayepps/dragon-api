

function DragonService() {
  this.name = 'DragonService';
  this.url = window.dragonSettings.apiUrl;
}

DragonService.prototype.ping = function() {
  $.ajax({
    url: this.url + '/api/ping',
    type: "GET",
    success: function (data) {
        console.log(data)
    }
  });
}

DragonService.prototype.get_all_todos = function(cb) {
  $.ajax({
    url: this.url + '/api/v1/todos',
    headers: {
        'x-api-key': window.dragonSettings.apiKey,
        'Content-Type':'application/json'
    },
    type: "GET",
    success: function (data) {
      cb(data.response);
    }
  });
}
