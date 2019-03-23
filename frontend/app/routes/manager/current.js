import Route from '@ember/routing/route';
import RSVP from 'rsvp';

export default Route.extend({
  model() {
    return RSVP.hash({
      tickets: this.store.findAll("ticket"),
      prices: this.store.findRecord("price", 1)
    });
  }
})
