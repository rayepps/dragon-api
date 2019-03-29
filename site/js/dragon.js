

url = ''

function GreenDragonService(url) {
  this.url = url;
}

GreenDragonService.prototype.ping = function() {
  $.ajax({
    url: this.url + '/api/ping',
    type: "GET",
    success: function (data) {
        console.log(data)
    }
  });
}



function Dragon() {
  console.log('hello');
}
