import Controller from '@ember/controller';

export default Controller.extend({
  actions: {
    create(payload) {
      let post = this.store.createRecord('ticket', {'numplate':payload});
      let self = this;
      function transitionToPost(post) {
        self.transitionToRoute('ticket-info', post.id)
      }
      function failure(reason) {
        alert(reason)
      }
      post.save().then(transitionToPost).catch(failure);

    }
  }
});
