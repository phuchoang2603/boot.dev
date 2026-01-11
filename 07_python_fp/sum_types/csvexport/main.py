from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status: CSVExportStatus, data: list):
    match status:
        case CSVExportStatus.PENDING:
            return (
                "Pending...",
                [list(map(lambda item: str(item), lst)) for lst in data],
            )
        case CSVExportStatus.PROCESSING:
            commas_join = map(lambda lst: ",".join(lst), data)
            newlines_join = "\n".join(commas_join)
            return ("Processing...", newlines_join)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            return (
                "Unknown error, retrying...",
                get_csv_status(
                    CSVExportStatus.PROCESSING,
                    get_csv_status(CSVExportStatus.PENDING, data)[1],
                )[1],
            )
        case _:
            raise Exception("unknown export status")
