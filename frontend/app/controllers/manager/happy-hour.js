import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    update(time) {
      if (confirm("Are you sure you want to set the time as " + time)) {
        this.store.findRecord('happy-hour', 1).then(function(post) {
          post.set('happyhour', time);
          post.save();
        })
      }
    }
  }
});
