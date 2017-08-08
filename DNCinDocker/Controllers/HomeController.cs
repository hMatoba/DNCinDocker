using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace DNCinDocker.Controllers
{
    public class HomeController : Controller
    {
        [Route("{*path}")]
        public IActionResult NotFound(string path)
        {
            Response.StatusCode = 404;
            return View();
        }
    }
}
