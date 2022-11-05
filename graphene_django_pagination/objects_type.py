from graphene import ObjectType, Boolean, Int


class PageInfoExtra(ObjectType):
    has_next_page = Boolean(
        required=True,
        name="hasNextPage",
        description="When paginating forwards, are there more items?",
    )

    has_previous_page = Boolean(
        required=True,
        name="hasPreviousPage",
        description="When paginating backwards, are there more items?",
    )

    total_pages = Int(
        required=True,
        name="totalPages",
        description="Total Number of pages for Pagination."
    )
