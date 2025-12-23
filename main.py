from GenAI_2_45 import ParagraphQAEvaluator

# Initialize the evaluator with default model
evaluator = ParagraphQAEvaluator()

path = "/Users/danielgehrman/Documents/Programming/Uni/Project-Class-25-26/3-GenAI43/pii.txt"

def extract_text_from_file(filepath: str) -> str:
    text = ""
    with open(filepath, "r") as f:
        f.read(text)
    
    return text

questions = [
    ["В каком году родился Андрей Климов?", "1989", 0],
    ["В каком городе родился Андрей Климов?", "Кострома", 0],
    ["Как звали отца Андрея Климова?", "Виктор Климов", 0],
    ["Кем работала мать Андрея?", "Бухгалтером в районной поликлинике", 0],
    ["У какой бабушки Андрей проводил лето в деревне?", "Лидии Павловны", 0],
    ["В какую школу пошёл Андрей?", "Школа №17", 1],
    ["Какие предметы давались Андрею лучше всего?", "Русский язык и история", 1],
    ["На какую специальность Андрей поступил в колледже?", "Документационное обеспечение управления", 2],
    ["Где было первое официальное место работы Андрея?", "Архив муниципального предприятия «ГорТрансСервис»", 3],
    ["В каком возрасте Андрей переехал в Ярославль?", "В 27 лет", 4]
]


# Load the QA model
if evaluator.load_model():

    for que, expected_answer, targ_par in questions:
        # Run the standard 3-paragraph test targeting the second paragraph
        result = evaluator.run_specific_test(que, expected_answer, target_paragraph=targ_par, document_path=path)
    
        # Generate comprehensive report
        evaluator.print_test_report(result)
        
        # Save results
        evaluator.save_results(result, "results/my_test.json")
