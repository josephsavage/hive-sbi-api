from django.core.management.base import BaseCommand
from hive_sbi_api.core.models import Post, PostVotes

BATCH_SIZE = 500

class Command(BaseCommand):
    help = "Backfill core_post_votes from core_post JSON fields"

    def handle(self, *args, **options):
        last_id = 0

        while True:
            posts = (
                Post.objects
                .filter(id__gt=last_id)
                .order_by("id")[:BATCH_SIZE]
            )

            if not posts:
                self.stdout.write(self.style.SUCCESS("Backfill complete"))
                return

            for post in posts:
                last_id = post.id

                # Skip if already migrated
                if hasattr(post, "votes_payload"):
                    continue

                PostVotes.objects.create(
                    post=post,
                    active_votes=post.active_votes,
                    beneficiaries=post.beneficiaries,
                )

            self.stdout.write(f"Processed up to Post ID {last_id}")
