import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

import { initAmplify } from './core/auth/amplify-config';

initAmplify();

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
