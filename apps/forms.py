from django import forms


# 表单基类
class FormMixin(object):
    # 格式化错误信息
    def get_errors(self):
        errors: dict = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors
