from ansible.plugins.action import ActionBase
import jinja2
import ast


class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        args = self._task.args.copy()
        if 'strint_to_eval' not in args:
            args['string_to_eval'] = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
        return_value = {
            "value": ast.literal_eval(args['string_to_eval'])
        }
        return dict(return_value)


