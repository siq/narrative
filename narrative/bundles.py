from mesh.standard import Bundle, mount

from narrative import resources

API = Bundle('narrative',
    mount(resources.Entry, 'narrative.controllers.entry.EntryController'),
    mount(resources.Notification, 'narrative.controllers.notification.NotificationController'),
)
