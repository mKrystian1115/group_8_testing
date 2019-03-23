import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('login');
  this.route('ticket-info', { path: '/ticket-info/:ticket_id' });

  this.route('manager', function() {
    this.route('current');
    this.route('happy-hour', { path: '/happy' });
    this.route('price');
    this.route('statistics');
    this.route('menu');
  });

});

export default Router;
