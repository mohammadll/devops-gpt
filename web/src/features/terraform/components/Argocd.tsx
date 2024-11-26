import { useEffect, useState } from "react";
import { cn } from "../../../utils/tailwind";
import { FaChevronDown } from "react-icons/fa";
import apiClient from "../../../utils/apiClient";
import { Endpoints } from "../../constants";
import { useMutation } from "@tanstack/react-query";

const Argocd = () => {
  const [buttons, setButtons] = useState({
    auto_prune: false,
    self_heal: false,
    argocd_repository: false,
    application_depends_repository: false
  });

  const [menus, setMenus] = useState({
    argocd_application: false,
    sync_policy: false
  });

  const [error, setError] = useState(false);

  const {data, isPending, isError, isSuccess, mutate} = useMutation<{output: string}, Error, {body: {argocd_application: {sync_policy: {auto_prune: boolean, self_heal: boolean}}, argocd_repository: boolean, application_depends_repository: boolean}}>({
    mutationKey: ["argocd"],
    mutationFn: async ({body}) => {
       return await apiClient.post(Endpoints.POST_IAC_ARGOCD, {...body});
    }
  })

  useEffect(() => {
    if (isError) {
      setError(true);
      setTimeout(() => {
        setError(false);
      }, 3000);
    }
  }, [isError]);

  useEffect(() => {
    if (isSuccess && data) {
      const {output} = data;
      const link = document.createElement('a');
      link.href = output;
      document.body.appendChild(link);
      link.click();

      document.body.removeChild(link);

    }
  }, [isSuccess, data])

  const handleButtons = (button: keyof typeof buttons) => {
    setButtons({...buttons, [button]: !buttons[button]})
  }

  const handleMenus = (menu: keyof typeof menus) => {
    setMenus({...menus, [menu]: !menus[menu]})
  }

  const handleSubmit = async () => {
      const body = {
        "argocd_application": {
          "sync_policy": {
            "auto_prune": buttons.auto_prune,
            "self_heal": buttons.self_heal
          }
        },
        "argocd_repository": buttons.argocd_repository,
        "application_depends_repository": buttons.application_depends_repository
      }
     
      mutate({body})
  }

  return (
    <div className="flex flex-col items-center justify-center">
      <div className="w-full bg-orange-800 divide-y-2 divide-gray-300 rounded-md max-w-96">
        <div className="divide-y-2 divide-gray-300">
          <button className="flex items-center justify-between w-full px-4 py-2" onClick={() => handleMenus("argocd_application")}>
            <p>Argocd Application</p>
            <FaChevronDown className={cn('transition-all', {"rotate-180": menus.argocd_application})} />
          </button>
          <div className={cn("divide-y-2 divide-gray-300 max-h-0 overflow-hidden transition-all ease-linear duration-300", {"max-h-96": !menus.argocd_application})}>
            <button className="flex items-center justify-between w-full py-2 pl-10 pr-4" onClick={() => handleMenus("sync_policy")}>
            <p>Sync Policy</p>
            <FaChevronDown className={cn('transition-all', {"rotate-180": menus.sync_policy})} />
          </button>
            <div className={cn("divide-y-2 divide-gray-300 max-h-0 overflow-hidden transition-all ease-linear duration-300", {"max-h-96": !menus.sync_policy})}>
              <div className="py-2 pl-16 pr-4">
                <div className="flex items-center justify-between">
                  <p>Auto Prune</p>
                  <input type="checkbox" className={cn('border-orange-[#2e323a] toggle [--tglbg:#2e323a] bg-orange-300 hover:bg-orange-400', {
                  'bg-[#5b6372] hover:bg-[#5b6372]': !buttons.auto_prune,
                }) } checked={buttons.auto_prune} onClick={() => handleButtons("auto_prune")} />
                </div>
              </div>
              <div className="py-2 pl-16 pr-4">
                <div className="flex items-center justify-between">
                  <p>Self Heal</p>
                  <input type="checkbox" className={cn('border-orange-[#2e323a] toggle [--tglbg:#2e323a] bg-orange-300 hover:bg-orange-400', {
                  'bg-[#5b6372] hover:bg-[#5b6372]': !buttons.self_heal,
                }) } checked={buttons.self_heal} onClick={() => handleButtons("self_heal")} />
                </div>
              </div>
            </div>
          </div>
          <div className="px-4 py-2">
            <div className="flex items-center justify-between">
              <p>Argocd Repository</p>
              <input type="checkbox" className={cn('border-orange-[#2e323a] toggle [--tglbg:#2e323a] bg-orange-300 hover:bg-orange-400', {
                'bg-[#5b6372] hover:bg-[#5b6372]': !buttons.argocd_repository,
              }) } checked={buttons.argocd_repository} onClick={() => handleButtons("argocd_repository")} />
            </div>
          </div>
          <div className="px-4 py-2">
            <div className="flex items-center justify-between">
              <p>Application Depends Repository</p>
              <input type="checkbox" className={cn('border-orange-[#2e323a] toggle [--tglbg:#2e323a] bg-orange-300 hover:bg-orange-400', {
                'bg-[#5b6372] hover:bg-[#5b6372]': !buttons.application_depends_repository,
              }) } checked={buttons.application_depends_repository} onClick={() => handleButtons("application_depends_repository")} />
            </div>
          </div>
        </div>
      </div>
      <button disabled={isPending} onClick={handleSubmit} className="w-full py-2 mt-4 text-center transition-all bg-orange-800 rounded-md btn max-w-96 hover:bg-orange-900">{isPending ? <div className="flex items-center justify-center gap-4 disabled:opacity-80"><span className="loading loading-spinner"></span>Loading</div>: error ? "Error" : "Submit"}</button>
    </div>
  );
};

export default Argocd;
