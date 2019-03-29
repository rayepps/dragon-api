

function TaskListController($elem, services) {

  this.$elem = $elem;
  this.dragon = services.findByProperty('name', 'DragonService');
  this.templator = services.findByProperty('name', 'TemplateService');

  this.dragon.get_all_todos(this.display_todos.bind(this))

}

TaskListController.prototype.display_todos = function(todos) {

  console.log('HERE');
  console.log(todos);

  todos.forEach(function(todo) {

    var html = this.templator.template('task', todo);
    var $todo = $(html);
    this.$elem.append($todo);

    new TaskController($todo, this.services)

  }.bind(this));

}
