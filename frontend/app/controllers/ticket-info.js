import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    update(ticket_id) {
      this.store.findRecord("ticket", ticket_id).then(function(post) {
        post.set("paid", true);
        post.save();
      })
    }
  }
});
