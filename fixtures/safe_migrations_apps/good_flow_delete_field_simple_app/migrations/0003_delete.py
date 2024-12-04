from sentry.new_migrations.migrations import CheckedMigration
from sentry.new_migrations.monkey.fields import SafeRemoveField
from sentry.new_migrations.monkey.state import DeletionAction


class Migration(CheckedMigration):
    dependencies = [
        ("good_flow_delete_field_simple_app", "0002_set_pending"),
    ]

    operations = [
        SafeRemoveField(
            model_name="testtable",
            name="field",
            deletion_action=DeletionAction.DELETE,
        ),
    ]