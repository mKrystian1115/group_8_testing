import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    update(price) {
      if (confirm("Are you sure you want to set the price as £" + price)) {
        this.store.findRecord('price', 1).then(function(post) {
          post.set('price', price);
          post.save();
        })
      }
    }
  }
});
