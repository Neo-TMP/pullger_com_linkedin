def getListOfExperience(squirrel):
    resultData = [];

    experienceSection = squirrel.finds_XPATH('//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "]')

    for curSection in experienceSection:
        expSection = curSection.find_XPATH('.//div[@id="experience"]');
        if expSection != None:
            experienceList = curSection.finds_XPATH(".//li[@class='artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column']")

            for curExperience in experienceList:

                experienceData = {};
                experienceData["companyID"] = None
                experienceData["job_discription"] = None
                experienceData["companyName"] = None
                experienceData["job_timing_type"] = None
                experienceData["companyURL"] = None

                JobDiscriptionEl = curExperience.find_XPATH('.//div[@class="display-flex align-items-center"]//span[@aria-hidden="true"]')
                if JobDiscriptionEl != None:
                    experienceData["job_discription"] = JobDiscriptionEl.text;

                JobUrlEl = curExperience.find_XPATH('.//a[@data-field="experience_company_logo"]')
                if JobUrlEl != None:
                    href = experienceData["companyURL"] = JobUrlEl.get_attribute('href')

                    splitedUrl = list(filter(None,href.split("/")))
                    try:
                        experienceData["companyID"] = int(splitedUrl[-1])
                    except:
                        continue;

                JobNameEl = curExperience.find_XPATH('.//span[@class="t-14 t-normal"]/span[@aria-hidden="true"]')
                if JobNameEl != None:
                    JobNameSplited = JobNameEl.text.split("·")
                    experienceData["companyName"] = JobNameSplited[0]

                    if len(JobNameSplited) > 1:
                        experienceData["job_timing_type"] = JobNameSplited[1];


                resultData.append(experienceData)

    return resultData
