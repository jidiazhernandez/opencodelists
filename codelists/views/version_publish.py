from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from .. import actions
from .decorators import load_version, require_permission


@require_POST
@login_required
@load_version
@require_permission
def version_publish(request, version):
    # We want to redirect to the now-published Version after publishing it, but
    # the in-memory instance in this view won't be updated by the .save() call
    # inside the action.  So instead we return the new instance from the action
    # and use that.
    version = actions.publish_version(version=version)

    return redirect(version)