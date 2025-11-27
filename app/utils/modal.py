class Modal(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Modal, cls).__new__(cls)
        return cls.__instance

    def show_modal(self, session, title, message):
        session['title'] = title
        session['message'] = message

    def clear_modal(self, session):
        session.pop('title', None)
        session.pop('message', None)