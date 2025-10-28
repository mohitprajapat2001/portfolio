# Initials Command to setup required initials data
from django.core.management.base import BaseCommand
from aboutme.models import (
    Profile,
    Address,
    Skills,
    Technology,
    Project,
    Company,
    Experience,
)
from django.conf import settings
import json
from logging import getLogger
from cities_light.models import City, Country, Region

logger = getLogger(__name__)


def _load_fixtures_data(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Fixture file not found: {file_path}")
        return None


def _bulk_create_technologies():
    fixtures_data = _load_fixtures_data(settings.TECHNOLOGY_FIXTURE_DIRS)
    if fixtures_data:
        technologies = [Technology(**data) for data in fixtures_data]
        Technology.objects.bulk_create(technologies)
        print("Technologies created successfully.")
    else:
        logger.error("Failed to create technologies.")


class Command(BaseCommand):
    help = "Initialize required initials data for the application"

    def handle(self, *args, **kwargs):
        # Create a default profile if it doesn't exist
        if not Profile.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            Profile.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD,
            )
        # Create Technology entries
        _bulk_create_technologies()

        # User Profile Create
        profile = _load_fixtures_data(settings.PROFILE_FIXTURE_DIRS)
        if not profile:
            logger.error("Failed to load profile data.")
            self.stderr.write("Failed to load profile data.")
            return
        if not Profile.objects.filter(username=profile["username"]).exists():
            profile, _ = Profile.objects.update_or_create(
                username=profile["username"],
                first_name=profile["first_name"],
                last_name=profile["last_name"],
                email=profile["email"],
                phone=profile["phone"],
            )
            profile.set_password(settings.USER_PASSWORD)
            profile.save()
            print("Profile created successfully.")
        profile = Profile.objects.get(username=profile["username"])

        # Create Address
        address_data = _load_fixtures_data(settings.ADDRESS_FIXTURE_DIRS)
        if address_data:
            for address in address_data:
                Address.objects.update_or_create(
                    profile=profile,
                    street_address=address["street_address"],
                    city=City.objects.filter(
                        search_names__contains=address["city"]
                    ).first(),
                    region=Region.objects.filter(
                        name__contains=address["region"]
                    ).first(),
                    country=Country.objects.first(),
                    postal_code=address["postal_code"],
                )
            print("Address created successfully.")
        else:
            logger.error("Failed to load address data.")

        # Create Skills
        skill_data = _load_fixtures_data(settings.SKILLS_FIXTURE_DIRS)
        if skill_data:
            for skill in skill_data:
                Skills.objects.update_or_create(
                    profile=profile,
                    name=skill["name"],
                    proficiency=skill["proficiency"],
                )
            print("Skills created successfully.")
        else:
            logger.error("Failed to load skill data.")
        # Create Companies
        company_data = _load_fixtures_data(settings.COMPANY_FIXTURE_DIRS)
        if company_data:
            for data in company_data:
                Company.objects.update_or_create(
                    title=data["title"],
                )
            print("Companies created successfully.")
        else:
            logger.error("Failed to load company data.")

        # Create Experiences
        experience_data = _load_fixtures_data(settings.EXPERIENCE_FIXTURE_DIRS)
        if experience_data:
            for data in experience_data:
                company = Company.objects.filter(
                    title__contains=data["company"]
                ).first()
                Experience.objects.update_or_create(
                    role=data["role"],
                    company=company,
                    start_date=data["start_date"],
                    end_date=data.get("end_date") if data.get("end_date") else None,
                    description=data["description"],
                    is_current=data["is_current"],
                )
            print("Experiences created successfully.")
        else:
            logger.error("Failed to load experience data.")

        # Create Projects
        project_data = _load_fixtures_data(settings.PROJECT_FIXTURE_DIRS)
        if project_data:
            for data in project_data:
                project, _ = Project.objects.update_or_create(
                    profile=profile,
                    title=data["title"],
                    description=data["description"],
                )
                project.technologies.set(
                    Technology.objects.filter(name__in=data["technologies"])
                )
            print("Projects created successfully.")
        else:
            logger.error("Failed to load project data.")
        self.stdout.write(
            self.style.SUCCESS("Initial data setup completed successfully.")
        )
