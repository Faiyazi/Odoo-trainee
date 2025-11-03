import { registry } from '@web/core/registry';

registry.category("services").add('my-service',{
    dependencies : ['notification'],
    start(env,{ notification }) {
        setInterval(() => notification.add("hello"), 5000);
        console.log('hello is sevieces')
    }
});